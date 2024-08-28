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
          'security/groups.xml',
        'views/course_views.xml',
        'views/teacher_views.xml',
        'views/student_views.xml',
        'views/group_views.xml',
        'views/payment_views.xml',
        'security/ir.model.access.csv',
      
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}