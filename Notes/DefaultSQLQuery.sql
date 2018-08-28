select * from 网站职员表
insert into 网站职员表(职员编号,姓名,年龄,工资,毕业院校) values(9,'小金',27,3000,'复旦大学')
delete from 网站职员表 where 姓名='小金'
sp_settriggerorder @triggername='testTriggerF',@order='first',@stmttype='insert'
create trigger testInsteadTriggerA on 网站职员表 instead of delete as
alter trigger tirggerTestInsertA on 网站职员表 for insert as
update 网站经营项目表 set 项目名称='软件开发'
exec sp_help testInsteadTriggerA
exec sp_helptext testInsteadTriggerA
xp_instance_regwrite N'HKEY_LOCAL_MACHINE',N'SOFTEWARE\Microsoft\Microsoft SQL Server','LoginMode',N'REG_DWORD',2
exec sp_password 'Oldpsd','Newpsd','Account'
exec sp_defaltdb 'Account','NewDb'
exec sp_defaltlanguage 'Account','Language'
exec sp_droplogin 'Account'
exec sp_grantdbaccess 'Account','UserName'
exec sp_helpuser 'UserName'
exec sp_revokedbaccess 'UserName'
exec sp_addsrvrolemember 'Loginame','RoleName'
exec sp_dropsrvrolemember 'Loginame','RoleName'
exec sp_addrole 'RoleName','RoleOwner'
exec sp_droprole 'RoleName'
exec sp_addrolemember 'RoleName','RoleAdder'
exec sp_droprolemember 'RoleName','RoleAdder'
grant update on TableName to UserName with grant option
grant insert on TableName to UserName
revoke update on TableName from UserName cascade
deny update on TableName to UserName cascade
backup database DbName to disk=N'FilePath' WITH NOFORMAT,NOINIT,NAME=N'FileName',SKIP,NOREWIND,STATS=10
backup database DbName to disk=N'FilePath' WITH DIFFNOFORMAT,NOFORMAT,NOINIT,NAME=N'FileName',SKIP,NOREWIND,NOUNLOAD,STATS=10
backup log database DbName to disk=N'FilePath' WITH NOFORMAT,NOINIT,NAME=N'FileName',SKIP,NOREWIND,NOUNLOAD,STATS=10
restore database DbName from to disk=N'FilePath' with file=1,nounload,stats=10
