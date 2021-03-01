# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PersonRecord(models.Model):
    _name = 'person.record'
    _description = "person"

    name = fields.Char(string='姓名')
    date = fields.Date(string='确证日期')
    state = fields.Char(string='省份')
    city = fields.Char(string='去')
    street = fields.Char(string='具体地址')
    ill_type = fields.Char(string='感染方式')
    within_or_abroad = fields.Selection([('within','境内'),('abroad', '境外')], string='境内/境内感染')

