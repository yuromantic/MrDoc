from django.urls import path,re_path
from app_admin import views

urlpatterns = [
    path('user_manage/',views.admin_user,name="user_manage"),  # 用户管理页面
    path('user_profile/',views.admin_user_profile, name="user_profile"), # 用户资料页面
    path('api/users', views.AdminUserList.as_view(), name="api_admin_users"),  # 用户列表接口
    path('api/user/<int:id>',views.AdminUserDetail.as_view(), name="api_admin_user"), # 用户接口

    path('modify_pwd',views.change_pwd,name="modify_pwd"),  # 普通用户修改密码

    path('project_manage/',views.admin_project,name='project_manage'), # 文集管理
    path('project_role_manage/<int:pro_id>/',views.admin_project_role,name="admin_project_role"), # 管理文集权限
    path('project_manage_istop',views.admin_project_istop,name="admin_project_istop"), # 修改文集置顶状态
    path('project_del/',views.admin_project_delete,name="admin_project_del"), # 删除文集

    path('doc_manage/',views.admin_doc,name='doc_manage'), # 文档管理
    path('doctemp_manage/',views.admin_doctemp,name='doctemp_manage'), # 文档模板管理
    path('setting/',views.admin_setting,name="sys_setting"), # 应用设置
    path('forget_pwd/',views.forget_pwd,name='forget_pwd'), # 忘记密码
    path('send_email_vcode/',views.send_email_vcode,name='send_email_vcode'), # 忘记密码发送邮件验证码
    path('admin_register_code/',views.admin_register_code,name='register_code_manage'), # 注册邀请码管理
    path('check_update/',views.check_update,name='check_update'), # 检测版本更新
    path('admin_center/',views.admin_center,name="admin_center"), # 后台管理
    path('admin/center_menu/',views.admin_center_menu,name="admin_center_menu"), # 后台管理菜单数据
    path('admin_overview/',views.admin_overview,name="admin_overview"), # 后台管理仪表盘

]