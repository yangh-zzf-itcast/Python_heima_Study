-- 数据库的基本操作

	-- 连接数据库
	mysql -uroot -p
	mysql -uroot -p123456 

	-- 退出数据库
	exit/quit/ctrl+d

	--sql语句最后需要分号；结尾
	--显示数据库版本
	select version();

	--显示时间
	select now();

	--查询所有数据库
	show databases;

	--创建数据库,并设置字符集
	create database pythonTest charset = utf8;

	--查看创建数据库的语句
	show create database pythonTest;

	--查看当前使用的数据库
	select datavase();

	--使用数据库
	use pythonTest;

	--删除数据库
	drop database pythonTest;

-- 数据表的基本操作	

	--显示表的结构
	--desc 数据表的名字；
	desc class;

	--查看当前数据库中的所有表
	show tables;

	--创建表
	--auto_increament 表示自动增长
	--not null 表示不能为空
	--primary key 表示主键
	--default 表示默认值
	--create table 数据表名(字段 类型 约束[, 字段 类型 约束]);
	create table class(id int, name varchar(30));
	create table class(
		id int primary key not null auto_increment, 
		name varchar(30)
	);

	--创建一个student表
	create table student2(
		id int unsigned not null auto_increment primary key,
		name varchar(30),
		age tinyint unsigned,
		high decimal(5, 2),
		gender enum("男", "女", "中性") default "保密",
		cls_id int unsigned
	);

	insert into student2 values(0, "老王", 18, 178.00, "男", 0);

	--创建一个class表
	create table class(
		id int unsigned not null auto_increment primary key,
		name varchar(30)
	);

	--查看表的创建语句
	show create table 表名字;

	--修改表-添加字段
	alter table student2 add birthday datetime;

	--修改表-修改字段--不重命名版,字段名不变
	--modify 字段名 类型及约束
	alter table student2 modify birthday date default "1995-08-20";

	--修改表-修改字段--重命名版,字段名改变
	--change 原字段名 新字段名 类型及约束
	alter table student2 change birthday birth date;

	--删除表-删除字段
	alter table student2 drop birth;

	--删除表
	drop table student2;


--增删改查(curd)-重点中的重点

	--增加
		--全列插入
		--insert into 表名 values(...)
		--主键字段 可以用 0 null default 来占位
		--向class表中插入一条数据
		insert into class values(0, "就业班");

		--向student2表中插入数据
		insert into student2 values(0, "杨航", 24, 179, "男"，2, "1995-07-25");
		
		--插入多条记录
		insert into student2 values(0, "杨航", 24, 179, "男"，2, "1995-07-25"), (0, "子繁", 25, 164, "女", 2, "1995-12-25");
		
		--部分插入
		--insert into 表名(字段名1,...) values (值,...)
		insert into student2(name, gender) values ("小乔", 2);
		--一次插入多个记录
		insert into student2(name, gender) values ("小乔", 2),("大乔", 2);

		--修改
		--update 表名 set 列1=值1,列2=值2...where 条件(主键);
		--全字段修改
		update student2 set gender = 2;
		--有条件的修改
		update student2 set age = 21, gender = 2 where id = 1;

		--实际开发中，谨慎使用删除，一般不使用
		--删了也不要修改auto_increment的值，否则之后容易崩溃
		--删除
			--物理删除
			--delete from 表名 where 条件;
			--清空数据表
			delete from student;

			--逻辑删除，不是真的删除，一般都使用这种方式
			--用一个字段来表示 1表示这条信息已经不能再使用了
			alter table students add is_delete bit default 0;
			update student2 set is_delete = 1 where name = "老王";

		--查用的最多
		--查询的基本使用
			--查询所有列，数据少的时候使用
			--select * from 表名;
			select * from student2;

			--指定条件查询
			select * from student2 where name = "杨航";
			

			--查询指定列
			select name, gender from student2;

			--字段的顺序
			--可以根据查询的顺序来修改，先查的排在前面
			select gender, name from student2;

			--可以用as为列或者表指定别名 
			--as也可以省略，直接在字段后面跟上别名
			select name as 姓名, gender as 性别 from student2;
