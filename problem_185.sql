-- Created by :Jiaming
-- Created at 2020-02-22


--Employee 表包含所有员工信息，每个员工有其对应的工号 Id，姓名 Name，工资 Salary 和部门编号 DepartmentId 。
--
--+----+-------+--------+--------------+
--| Id | Name  | Salary | DepartmentId |
--+----+-------+--------+--------------+
--| 1  | Joe   | 85000  | 1            |
--| 2  | Henry | 80000  | 2            |
--| 3  | Sam   | 60000  | 2            |
--| 4  | Max   | 90000  | 1            |
--| 5  | Janet | 69000  | 1            |
--| 6  | Randy | 85000  | 1            |
--| 7  | Will  | 70000  | 1            |
--+----+-------+--------+--------------+
--Department 表包含公司所有部门的信息。
--
--+----+----------+
--| Id | Name     |
--+----+----------+
--| 1  | IT       |
--| 2  | Sales    |
--+----+----------+
--编写一个 SQL 查询，找出每个部门获得前三高工资的所有员工。例如，根据上述给定的表，查询结果应返回：
--
--+------------+----------+--------+
--| Department | Employee | Salary |
--+------------+----------+--------+
--| IT         | Max      | 90000  |
--| IT         | Randy    | 85000  |
--| IT         | Joe      | 85000  |
--| IT         | Will     | 70000  |
--| Sales      | Henry    | 80000  |
--| Sales      | Sam      | 60000  |
--+------------+----------+--------+
--解释：
--
--IT 部门中，Max 获得了最高的工资，Randy 和 Joe 都拿到了第二高的工资，Will 的工资排第三。销售部门（Sales）只有两名员工，Henry 的工资最高，Sam 的工资排第二。
--
--来源：力扣（LeetCode）
--链接：https://leetcode-cn.com/problems/department-top-three-salaries
--著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

-- 准备表
CREATE TABLE `Department` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  ` Name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Employee` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) DEFAULT '',
  `Salary` int(11) DEFAULT '0',
  `DepartmentId` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入数据
insert into Department (id,`Name`) value (1,'IT');
insert into Department (id,`Name`) value (2,'Sales');



insert into Employee (`Id`,`Name`,`Salary`,`DepartmentId`) value (1,'Joe',85000,1);
insert into Employee (`Id`,`Name`,`Salary`,`DepartmentId`) value (2,'Henry',80000,2);
insert into Employee (`Id`,`Name`,`Salary`,`DepartmentId`) value (3,'Sam',60000,2);
insert into Employee (`Id`,`Name`,`Salary`,`DepartmentId`) value (4,'Max',90000,1);
insert into Employee (`Id`,`Name`,`Salary`,`DepartmentId`) value (5,'Janet',69000,1);
insert into Employee (`Id`,`Name`,`Salary`,`DepartmentId`) value (6,'Randy',85000,1);
insert into Employee (`Id`,`Name`,`Salary`,`DepartmentId`) value (7,'Will',70000,1);

-- 查询
-- 执行用时 :578 ms, 在所有 MySQL 提交中击败了69.31%的用户

select d.Name as Department,e.Name as Employee,e.Salary as Salary
from Employee as e join Department as d
on e.DepartmentId = d.Id
where e.Id in
(
    select e1.Id
    from Employee as e1 left join Employee as e2
    on e1.DepartmentId = e2.DepartmentId and e1.Salary < e2.Salary
    group by e1.Id
    having count(distinct e2.Salary) <= 2
)
order by d.Id asc,e.Salary desc;

--Employee表左连接自己 表1的雇员连接同部门比自己高薪水的雇员，如果比自己高的只有两个薪资，那自己就是前三的,
-- 当没有人薪资比自己高的时候left join保证了最高薪资被join。

-- 以下是官方题解： 使用了子连接，思路相同。
--执行用时 :634 ms, 在所有 MySQL 提交中击败了36.03%的用户

SELECT d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
FROM
    Employee e1
        JOIN
    Department d ON e1.DepartmentId = d.Id
WHERE
    3 > (SELECT
            COUNT(DISTINCT e2.Salary)
        FROM
            Employee e2
        WHERE
            e2.Salary > e1.Salary
                AND e1.DepartmentId = e2.DepartmentId
        )
;