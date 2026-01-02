# Copyright (C) 2025 Entidad Pública Empresarial Red.es
#
# This file is part of "dge-drupal-users (datos.gob.es)".
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-
from flask import Blueprint
import ckan.plugins.toolkit as toolkit

dgeDrupalUsers = Blueprint(
    'dgeDrupalUsers',
    __name__,
)

def unauthorized():
     # Avoid loops
    extra_vars = {u'code': [401], u'content': u'You are not authorized to access this page.', u'name': u'Access denied'}
    return toolkit.render('error_document_template.html', extra_vars), 401

dgeDrupalUsers.add_url_rule('/user_unauthorized', 'user_unauthorized', view_func=unauthorized)