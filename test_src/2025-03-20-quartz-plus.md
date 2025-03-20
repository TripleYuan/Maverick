---
layout: post
title: quartz-plus
slug: quartz-plus
date: 2025-03-20 17:51:01
status: publish
author: wuxiaoyuan
excerpt: Quartz-Plus是一个Quartz作业调度框架的增强工具，支持以注解方式快速创建Job和Trigger，提供了一套功能完备的可视化的任务调度管理系统。
categories: 
  - Dev
tags: 
  - Java
  - SpringBoot
---

在工作中，我经常会使用到 Quartz，一个开源的分布式任务调度框架。然而，尽管 Quartz 提供了强大的功能，我在使用过程中却遇到了一些痛点：

- Quartz 不支持注解的方式定义Job，这导致我们只能通过硬编码的方式创建`Job`和`Trigger`，并手动注册到 Quartz scheduler 中。
- ​Quartz 未提供任务调度管理界面。在实际工作中，我常常需要手动触发某个Job的执行，然而由于缺少管理页面，我们只能通过修改数据库中 trigger 的执行时间来间接触发 job 的执行，这显然不是一个高效的方式。

为了解决这些问题，提高开发效率，我基于 Spring 对 Quartz 进行了扩展，开发了一个名为 Quartz Plus 的工具库：

- 支持注解的方式快速定义`Job`和`Trigger`：使用 @QuartzJob 和 @QuartzTrigger 注解，我们可以快速地定义`Job`和`Trigger`，并且它们会自动注册到`Quartz Scheduler`中。
- 实现了一个带有管理界面的 Quartz 任务调度中心：该任务调度中心提供了完整的管理界面，包括 job 管理、Quartz 实例管理、用户管理等功能，使我们能够更方便地管理和监控任务调度。


项目源码地址：https://github.com/TripleYuan/quartz-plus.git

## 快速上手

### 部署Quartz任务调度系统

调度系统分为前端和后端两个项目，可以分开部署 **quartz-plus-scheduler-center**（调度服务） 和 **quartz-plus-web-console**（前端应用），也可将前端代码打包后的静态资源文件集成到 `quartz-plus-scheduler-center` 中。

**`quartz-plus-scheduler-center` 默认使用的是H2数据库，生产环境建议使用外部数据库，如 MySQL、PostgreSQL 等。**

系统内置了两个登录用户：

> 用户1：用户名为 admin，密码为 123456，拥有管理员权限。
>
> 用户2：用户名为 quartz，密码为 123456，仅具有普通用户权限。

### 注解式定义Job和Trigger

使用 **@QuartzJob** 和 **@QuartzTrigger** 注解快速定义 `Job`和`Trigger`：

```java
@QuartzJob(description = "打印 hello world")
@QuartzTrigger(cron = "0/10 * * * * ?")
public class HelloWorldJob implements Job {

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("hello world, current time: " + LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
    }
}
```

### SpringBoot应用接入

1. 引入最新版本

```xml
<dependency>
    <groupId>redcoder</groupId>
    <artifactId>quartz-plus-core</artifactId>
    <version>${quartzplus.latest.version}</version>
</dependency>
```

2. 在启用类上添加注解 `@QuartzJobScan`，并指定 job 类所在的包路径。

```java
@SpringBootApplication
@QuartzJobScan("redcoder.quartzplus.demo.job")
public class QuartzPlusDemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(QuartzPlusDemoApplication.class, args);
    }
}
```

3. 添加配置，指定注册中心服务地址

```yaml
quartz-job-scheduler:
  registry:
    # 调度服务注册地址（替换成你的IP和端口）
    register-url: http://localhost:32007/api/quartz-job-scheduler/instance/register
    # 调度服务取消注册地址（替换成你的IP和端口）
    unregister-url: http://localhost:32007/api/quartz-job-scheduler/instance/unregister
```
