use class;
CREATE TABLE accounts (
    acc_no INT PRIMARY KEY,
    acc_holder VARCHAR(50),
    bln DECIMAL(10,2)
);

CREATE TABLE transactions (
    tran_id INT AUTO_INCREMENT PRIMARY KEY,
    acc_no INT,
    tran_type VARCHAR(10),
    amt DECIMAL(10,2),
    tran_date DATETIME
);

insert into accounts values (101,"ravi",5000);
insert into accounts values (102,"abhi",3000);
insert into accounts values (105,"shiva",4000);

select * from accounts;

delimiter $$

create trigger bank_trans_tgr
after update
on accounts
for each row
begin 
     if new.bln > old.bln then
        
        insert into transactions
        (acc_no,tran_type,amt,tran_date)
        values
        (new.acc_no,'credit', new.bln - old.bln , now());
        
     elseif new.bln < old.bln then
     
         insert into transactions
         (acc_no,tran_type,amt,tran_date)
         values
         (new.acc_no,'debit',old.bln - new.bln , now());
         
     end if ;
end $$

delimiter ;     

update accounts
set bln = 5500
where acc_no=101;

select * from accounts;

select * from transactions;


-- 2

create table products(
    prod_id int primary key,
    prod_name varchar(50),
    stock int
);    

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    prod_id INT,
    qunty INT
);

INSERT INTO products
VALUES
(1, 'Laptop', 50),
(2, 'Mouse', 100),
(3,'speaker',70);

delimiter $$

create trigger reduce_prod_stock
after insert 
on sales
for each row
begin
      update products
      set stock = stock - new.qunty
      where prod_id = new.prod_id;
      
end $$

delimiter ;

insert into sales values (101,1,5);    

select * from products;
select * from sales;

-- 3

CREATE TABLE employee (
    e_id INT PRIMARY KEY,
    e_name VARCHAR(50),
    sal DECIMAL(10,2)
);

INSERT INTO employee
VALUES (1, 'Ravi', 30000);
INSERT INTO employee
VALUES (2, 'shiva', 45000);

delimiter $$

create trigger check_sal
before update
on employee
for each row
begin
	if new.sal <=0 then 
        signal sqlstate '45000'
        set message_text = 'Invalid salary';
    end if;
end $$

delimiter ;


update employee
set sal=40000
where e_id = 1;    
    
 update employee
 set sal=-5000
 where e_id=1;
 
 -- 4 prevent invalid marks
 
 create table students(
      stu_id int primary key,
      stu_name varchar(50),
      marks int
);


delimiter $$

create trigger check_stu_marks
before insert 
on students
for each row
begin
   
     if new.marks < 0 or new.marks >100 then
     
     signal sqlstate '45000' 
     set message_text = 'marks must be between 0 and 100';
     
     end if ;
     
end $$

delimiter ;

insert into students
values(1,'ravi',65);    

insert into students
values(2,'abhi',94);

insert into students
values(3,'raji',-5);

select * from students;
   

CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);   

 CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT
);

 CREATE TABLE department_summary (
    dept_id INT PRIMARY KEY,
    emp_count INT DEFAULT 0
);

INSERT INTO department
VALUES
(10, 'HR'),
(20, 'IT'),
(30, 'Sales');

INSERT INTO department_summary
(dept_id, emp_count)
VALUES
(10, 0),
(20, 0),
(30, 0);

delimiter $$

create trigger increase_employee_count
after insert on employees
for each row
begin

    update department_summary
    set emp_count = emp_count + 1
    where dept_id = new.dept_id;

end $$

delimiter ;

delimiter $$

create trigger decrease_employee_count
after delete on employees
for each row
begin

    update department_summary
    set emp_count = emp_count - 1
    where dept_id = old.dept_id ;

end $$

delimiter ;


INSERT INTO employees
VALUES
(101, 'Ravi', 10),
(102, 'Priya', 10),
(103, 'Arun', 20);

SELECT * FROM department_summary;

DELETE FROM employees
WHERE emp_id = 101;

SELECT * FROM department_summary;