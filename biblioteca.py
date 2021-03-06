# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 S&C (<http://salazarcarlos.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
 
 
from openerp import models, fields, api, _
 
class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
 
    name = fields.Char(string='Titulo', required=True,)
    description = fields.Text('Observacion')
    date = fields.Date(string='Fecha de registro')
    autor= fields.Char(string='Autor', required=True,)
    year= fields.Integer(string='Año', required=True,)
    typeL= fields.Char(string= 'Tipo', required=True,)