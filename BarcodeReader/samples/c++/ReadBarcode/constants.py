filename = 'IMG-20190909-WA0004-converted.pdf'
image = "image.jpg"
pattern = "(?s)(?=Value).*?(?=Hex)"
save_dir = 'images'
output_file = "data.csv"
headers = ["vendor code","Po No","Invocie No.","Date","GSTIN","total invocie amount",\
			"total value","vehicle no","SGST","IGST","CGST","Description of Goods",\
			"HSN","quantity","basic amount"]