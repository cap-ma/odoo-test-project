{
    'name': 'edu_center',
    'version': '1.0',
    'summary': 'Manage educational center courses, teachers, students, and payments',
    'description': """
        This module provides functionality to manage:
        - Courses
        - Teachers
        - Students
        - Groups
        - Payments
    """,
    'category': 'Education',
    'author': 'Capma',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['base'],


    'data': [
        
        'security/security.xml',  
   
        'views/course_views.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/teacher_payment_views.xml',
        'views/payment_chart_views.xml',
        'views/group_views.xml',
        'views/payment_views.xml',
        'security/ir.model.access.csv',
    ],

 
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,


    # 'assets': {
    #     'web.assets_backend_prod_only': [
    #         ('include', 'https://www.gstatic.com/charts/loader.js'),
    #     ],
    #     'web.assets_backend': [
    #         'edu_center/static/src/js/payment_chart_widget.js',
    #     ],
    # },

 
}