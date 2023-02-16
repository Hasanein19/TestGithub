from odoo import models , fields, api ,exceptions,_
import base64
import datetime


####################################### Sale Invoice Report ########################################

class ProducttSalesXLS(models.AbstractModel):
  _name='report.spreport.report_ppurchase_xls'
  _inherit='report.report_xlsx.abstract'

  def generate_xlsx_report(self, workbook, data, lines):

     format1=workbook.add_format({'font_size':12,'align':'Center','bold':True ,'bg_color':'#5D6D7E','border':True})
     format2=workbook.add_format({'font_size':6,'align':'Center','bold':True ,'bg_color':'#CACFD2','border':True})
     format3=workbook.add_format({'font_size':6,'align':'Center','bold':True ,'bg_color':'#5D6D7E','border':True})
     format4=workbook.add_format({'font_size':6,'align':'vcenter' ,'border':True , 'bg_color':'#CACFD2'})
     sheet= workbook.add_worksheet('Purchase sheet')
     sheet.merge_range(1,3,1,15,'Purchase Received/Billed Report',format1)
     sheet.merge_range(2,3,2,4,'from Date:',format2)
     sheet.merge_range(3,3,3,4,'to Date:',format2)
     sheet.set_column('D:P',10)
     sheet.set_column('J:J',12)
     sheet.set_column('I:I',16)

     row=4
     col=3


     sheet.write(row,col,'purchase Order',format3)

     col+=1
     sheet.write(row,col,'Product',format3)

     col+=1
     sheet.write(row,col,'Code',format3) 

     col+=1
     sheet.write(row,col,'PO Price',format3)

     col+=1
     sheet.write(row,col,'Stock code',format3)

     col+=1
     sheet.write(row,col,'Stock Date',format3)

     col+=1
     sheet.write(row,col,'Stock Received Quantity',format3) 

  

     col+=1
     sheet.write(row,col,'Bill Code',format3)

     col+=1
     sheet.write(row,col,'Bill Date',format3)

     col+=1
     sheet.write(row,col,'Bill Price',format3) 

     col+=1
     sheet.write(row,col,'Bill Quantity',format3)

     col+=1
     sheet.write(row,col,'Quantity difference ',format3)
     col+=1
     sheet.write(row,col,'Price/unit difference',format3)


     col=3
     row=4

     for obj in lines: 
      stock = self.env['account.move'].browse(obj.p_order.name)
      stocks = self.env['stock.picking'].search([('origin','=',obj.p_order.name)]) 
      order = self.env['account.move'].browse(obj.p_order.name)
      orders = self.env['purchase.order'].search([('name','=',obj.p_order.name)])

      for i in obj.invoice_line_ids: 
       for l in stocks:
        for h in l.move_ids_without_package:
        
         for m in orders:
           for j in m.order_line:
           
            

               row+=1
               sheet.write(row,col,obj.p_order.name,format4) 


               col+=1 
               sheet.write(row,col,j.product_id.name,format4)
               col+=1
               sheet.write(row,col,j.name,format4)
               col+=1
               sheet.write(row,col,j.price_unit,format4)
               
               
               
               col+=1
               sheet.write(row,col,l.name,format4)
               col+=1
               sheet.write(row,col,l.scheduled_date,format4)
               col+=1
               sheet.write(row,col,h.quantity_done,format4)

               

               col+=1
               sheet.write(row,col,obj.name,format4)
               col+=1
               sheet.write(row,col,obj.invoice_date,format4)
               col+=1 
               sheet.write(row,col,i.quantity,format4)
               col+=1
               sheet.write(row,col,i.price_unit,format4)
            

               col+=1
               sheet.write(row,col,((i.quantity)-(h.quantity_done)),format4)
               col+=1
               sheet.write(row,col,((i.price_unit )-(j.price_unit)),format4)


               col=3   