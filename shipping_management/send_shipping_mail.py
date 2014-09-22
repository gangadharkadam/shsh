from __future__ import unicode_literals
import frappe
from frappe.core.doctype.notification_count.notification_count import delete_notification_count_for
from frappe.core.doctype.user.user import STANDARD_USERS
from frappe.utils import cint

def get_mail_details():
	frappe.errprint("mail")
	message=get_message()
	send_mail_to_customer(message)


def get_details(self):
	pass


def get_message():
	message="""<table>
				<tr>
					<td>Source: Port Mumbai</td>
					<td>Destination: Port Elizabeth</td>
				</tr>
	            <tr>
	            	<td>From Date: 20-09-2014</td>
	            	<td>To Date: 30-09-2014</td>
	            </tr>
	            <tr>
	            	<td>Rate: 2000</td>
	            </tr>
	            </table><table><tr>Cuntainer 1</tr><tr>Container 2</tr></table>"""

	# for container in container_list:
	# 	message += """<tr>"""+container+"""</tr>"""
	message += """</table>"""

	return message
	
def send_mail_to_customer(message):
	from frappe.utils import get_fullname, get_url

	try:
		frappe.sendmail(\
			recipients="rohit.w@indictranstech.com",
			sender= frappe.db.get_value("User", frappe.session.user, "email"),
			subject="Shipping Order",
			message=message,
			bulk=True)
	except frappe.OutgoingEmailError:
		pass

