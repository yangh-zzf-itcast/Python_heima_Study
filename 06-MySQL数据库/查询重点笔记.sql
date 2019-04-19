--基本查询
	--查询所有字段
	--select * from 表名;
	select * from student;
	select * from classes;
	select id, name from classes;

	--查询指定字段
	--select 列1, 列2... from 表名;
	--select 表名.字段 ... from 表名;
	select name, age from student;
	select student.name, student.age from student;

	--使用as起别名
	select name as 姓名, age as 年龄 from student;
	select name 姓名, age 年龄 from student;

	--给表名起别名
	--给表起了别名之后就不能再使用原名
	select s.name, s.age from student as s;

	--消除重复行
	--distinct 关键字
	select distinct gender from student;
	--用分组也可以实现
	select gender from student group by gender;


--条件查询
	--select ... from 表名 where...;
	--比较运算符 >, <, <=, >=, =, !=或<>
	select * from student where age>18;
	select name, gender from student where age<30;
	
	--逻辑运算符 and, or, not
	select * from student where age>18 and age<30;
	select * from student where not (age>18 and gender=2);

    --模糊查询,匹配符
		--like, 效率低
		-- % 替换一个或者多个
		-- _ 替换1个
		--查询姓名中 以“大”开头的名字
		select * from student where name like "大%";
		--查询姓名中有大的所有名字
		select * from student where name like "%大%";

		--查询有两个字的名字
		select * from student where name like "__";
		--至少两个字的名字
		select * from student where name like "__%";

		--rlike 正则
		--查询姓名中 以“大”开头的名字
		select * from student where name rlike "^大.*";
		--查询姓名中 以“大”开头,"伟"结尾的名字
		select * from student where name rlike "^大.*伟$";


	--范围查询
		--in(1,3,8)表示在一个非连续的范围内
		select name, age from student where age in (18,35,40);
		--not in(1,3,8) 不在一个非连续的范围内

		--between ... and ...表示在一个连续的范围内
		select name, age from student where age between 10 and 30;
		--not between ... and ... 表示不在连续的范围内
	
	--空判断
		--is null
		--判断身高为空的记录
		select * from student where height is null;

		--is not null

--排序
	--order by 字段
	--asc从小到大，顺序 默认
	--desc从大小小，倒序

	--查询年龄在18-40之间的男性，按照年龄从大到小排
	select * from student where (age between 18 and 40) and gender = 1 order by age desc;

	--order by 多个字段
	--查询年龄在18-40之间的男性，按身高从高到矮排序，如果身高相同的，按年龄从小到大排
	select * from student where (age between 18 and 40) and gender = 1 order by height desc, age;

	--按照年龄从小到大，身高从高到矮，前两个都相等按id排序；
	select * from student order by age, height desc, id;


--聚合函数
	--总数 count
	--查询女性多少人，男性多少人
	select * from student where gender=1;
	select count(*) as 男性人数 from student where gender=1;

	--最大值 max
	--查询最大的年龄
	select max(age) from student;

	--最小值 min
	--查询女性身高最小值
	select min(height) from student where gender=2;

	--求和 sum
	select sum(age) from student;

	--平均值 avg
	select avg(age) from student;
	select sum(age)/count(*) from student;

	--四舍五入 round(123.12, 1) 保留一位小数
	--计算所有人的平均年龄，保留两位小数
	select round(avg(age), 2) from student;

	--银行的数据中是不允许四舍五入的，不用小数点存储，会有误差
	--如果有小数点，例如3.14，直接乘100再存入数据库，要用了取出来再除以100

--分组
	--group by
	--按照性别分组，查询所有的性别
	select ... from student group by gender;

	--计算每种性别中的人数
	select gender, count(*) from student group by gender;

	--统计男性的人数
	select gender, count(*) from student where gender=1 group by gender;

	--显示每一组内全部的特定信息，group_concat(字段,...)
	select gender, group_concat(name) from student group by gender;
	--group_concat中也可以加自己的字符串
	select gender, group_concat(name,"_",age,"_",id) from student where gender=1 group by gender;

	--having 对分组后的查询结果进行筛选判断
	--where是对原始表的条件判断，两者的区别
	--查询平均年龄超过30的性别，以及姓名
	select gender, group_concat(name), avg(age) from student group by gender having avg(age)>30;

	--查询每种性别中的人数多于2个的信息
	select gender, group_concat(name) from student group by gender having count(*)>2;


--分页
	--limit, start, count
	--每页限制显示2个数据
	select * from student limit 2;
	--start=0，表示查询开始的记录，count=5，表示要查询的记录数
	--查询前5个数据
	select * from student limit 0,5;
	--下一页，5条记录一页，很多网站的页码也是这样做的
	--查询id6-10的数据
	select * from student limit 5,5;

	--每页显示2个，第1个页面
	select * from student limit 0,2;
	
	--每页显示2个，第2个页面
	select * from student limit 2,2;
	
	--每页显示2个，第3个页面
	select * from student limit 4,2;
	
	--每页显示2个，第4个页面
	select * from student limit 6,2; -- --->limit(第N页-1)*每页记录数，每页记录数;

	--每页显示2个，显示第6页的信息，按照年龄从小到大排序
	--失败select * from student limit 2*(6-1),2;
	--失败select * from student limit 10,2 order by age asc;
	--limit必须放在最后
	select * from student order by age limit 10,2;

--连接查询
	--内连接 inner join ... on
	select * from student inner join classes;
	--查询 由能够对应班级的学生以及班级信息
	select * from student inner join classes on student.cls_id = classes.id;
	--按要求显示姓名和班级
	select student.*, classes.name from student inner join classes on student.cls_id = classes.id;

	--起别名
	select stu.*, cls.name from student stu inner join classes cls on stu.cls_id = cls.id;

	--左外连接 left join ... on
	--取左边表的全部与 左右表的交集
	--查询每位学生对应的班级信息
	select * from student s left join classes c on s.cls_id=c.id;

	--右外连接 right join ... on
	--将左外连接的两个表顺序换一下就行

	--查询没有对应班级信息的学生
	select * from student s left join classes c on s.cls_id=c.id having c.id is NULL;

--自连接查询
	--思路就是相同表结构的多张表可以存储在一张表内
	--查询时，给这张表命名两个别名，当做两张表来做inner join ... on

	--查看中国有哪些省份
	select * from china where pid=0;   

	--查看浙江省有哪些市
	select province.atitle, city.atitle from china as province inner join china as city on city.pid=province.aid having province.atitle="浙江省"; 

	--查看宁波市有哪些区
	select city.atitle, area.atitle from china as city inner join china as area on city.aid=area.pid having city.atitle="宁波市";

--子查询
	--标量子查询
	--将一个查询的结果作为一个表结果给另一个查询
	--查询出高于平均身高的信息
	select * from student where height>(select avg(height) from student);

	--查询最高的男生的信息
	select * from student where height=(select max(height) from student where gender=1);
