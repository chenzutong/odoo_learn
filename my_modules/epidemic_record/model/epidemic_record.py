# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EpidemicRecord(models.Model):
    _name = 'epidemic.record'

    def _default_create_user_id(self):
        return self.env.uid

    # 姓名、日期、省、市、区/县、性别、年龄、就业状态、具体地址、感染方式、境内/境外感染
    name = fields.Char(string='姓名')
    date = fields.Date(string='确证日期')
    state = fields.Char(string='省份')
    city = fields.Char(string='市')
    county = fields.Char(string='区/县')
    street = fields.Char(string='具体地址')
    ill_type = fields.Char(string='感染方式')
    within_or_abroad = fields.Selection([('within', '境内'), ('abroad', '境外')], default='within', string='境内/境内感染')
    is_ill = fields.Boolean(string='是否确诊', default=False)
    begin_lsolation_date = fields.Date(string='起始隔离日期')
    lsolation_mode = fields.Selection([('home', '居家隔离'), ('focus', '集中隔离')], string='隔离方式')
    create_user_id = fields.Many2one('res.users', string='填报人', default=_default_create_user_id)
    note = fields.Text(string='说明')
    test_float = fields.Float(string='测试浮点字段')
    test_int = fields.Integer(string='测试整型字段')
