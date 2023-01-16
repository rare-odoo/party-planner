# -*- coding: utf-8 -*-

{
    'name':'Party Planner',
    'version':'1.0',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/party_planner_views.xml',
        'views/party_planner_type_views.xml',
        'views/party_planner_tag_views.xml',
        'views/city_views.xml',
        'demo/party_planner_tags_demo_data.xml',
        'demo/party_planner_types_demo_data.xml',
        'demo/indian_cities.xml',
        'views/party_planner_menu_views.xml',
    ],
    'author':'rare',
    'category':'sap',
    'description':'This is a Party Planner Application where people can handle their parties hassle free 😎',
    'installable':'True',
    'application':'True'
}