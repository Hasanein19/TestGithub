from odoo import models , fields, api ,exceptions,_
import base64


####################################### Sale Invoice Report ########################################

class ProducttSalesXLS(models.AbstractModel):
  _name='report.spreport.report_ssale_xls'
  _inherit='report.report_xlsx.abstract'

  def generate_xlsx_report(self, workbook, data, lines):

	  format1=workbook.add_format({'font_size':12,'align':'Center','bold':True ,'bg_color':'#5D6D7E','border':True})
	  format2=workbook.add_format({'font_size':6,'align':'Center','bold':True ,'bg_color':'#CACFD2','border':True})
	  format3=workbook.add_format({'font_size':6,'align':'Center','bold':True ,'bg_color':'#5D6D7E','border':True})
	  format4=workbook.add_format({'font_size':6,'align':'vcenter' ,'border':True , 'bg_color':'#CACFD2'})
	  sheet= workbook.add_worksheet('Sale sheet')
	  sheet.merge_range(1,3,1,15,'Sale Delivered/Invoiced Report',format1)
	  sheet.merge_range(2,3,2,4,'from Date:',format2)
	  sheet.merge_range(3,3,3,4,'to Date:',format2)
	  sheet.set_column('D:P',10)
	  sheet.set_column('J:J',12)
	  sheet.set_column('I:I',16)


	
	  row=4
	  col=3
	  sheet.write(row,col,'Sale Order',format3)

	  col+=1
	  sheet.write(row,col,'Product',format3)

	  col+=1
	  sheet.write(row,col,'Code',format3) 

	  col+=1
	  sheet.write(row,col,'SO Price',format3)

	  col+=1
	  sheet.write(row,col,'Stock code',format3)

	  col+=1
	  sheet.write(row,col,'Stock Date',format3)

	  col+=1
	  sheet.write(row,col,'Stock Delivered Quantity',format3) 


	  col+=1
	  sheet.write(row,col,'Invoice Code',format3)

	  col+=1
	  sheet.write(row,col,'Invoice Date',format3)

	  col+=1
	  sheet.write(row,col,'Invoice Price',format3) 

	  col+=1
	  sheet.write(row,col,'Invoice Quantity',format3)

	  col+=1
	  sheet.write(row,col,'Quantity difference ',format3)
	  col+=1
	  sheet.write(row,col,'Price/unit difference',format3)


	  col=3
	  row=4

	  for objj in lines: 
	  
	   stockk= self.env['account.move'].browse(objj.s_order.name)
	   stockks =self.env['stock.picking'].search([('origin','=',objj.s_order.name)])
	   orderr= self.env['account.move'].browse(objj.s_order.name)
	   orderrs= self.env['sale.order'].search([('name','=',objj.s_order.name)]) 

	   for ii in objj.invoice_line_ids: 
	   	for ll in stockks:
	   	 for hh in ll.move_ids_without_package:

	   	  for mm in orderrs:
	   	 	 for jj in mm.order_line:
	  
	  
	   	 	 		row+=1
	   	 	 		sheet.write(row,col,objj.s_order.name,format4)


	   	 	 		col+=1 
	   	 	 		sheet.write(row,col,jj.product_id.name,format4)
	   	 	 		col+=1
	   	 	 		sheet.write(row,col,jj.name,format4)
	   	 	 		col+=1
	   	 	 		sheet.write(row,col,jj.price_unit,format4)

	   	 	 		col+=1
	   	 	 		sheet.write(row,col,ll.name,format4)
	   	 	 		col+=1
	   	 	 		sheet.write(row,col,ll.scheduled_date,format4)
	   	 	 		col+=1
	   	 	 		sheet.write(row,col,hh.quantity_done,format4)

	   	 	 		col+=1
	   	 	 		sheet.write(row,col,objj.name,format4)
	   	 	 		col+=1
	   	 	 		sheet.write(row,col,objj.invoice_date,format4)
	   	 	 		col+=1 
	   	 	 		sheet.write(row,col,ii.quantity,format4)
	   	 	 		col+=1
	   	 	 		sheet.write(row,col,ii.price_unit,format4)

	   	 	 		col+=1
	   	 	 		sheet.write(row,col,((ii.quantity )- (hh.quantity_done)),format4)
	   	 	 		col+=1
	   	 	 		sheet.write(row,col,((ii.price_unit)-(jj.price_unit)),format4)

 	 	 		

	   	 	 		col=3  
	   	
