from openpyxl import Workbook

def create_excel():
    """Write to an excel file"""
    workbook = Workbook()
    worksheet = workbook.create_sheet("Cities", 0)

    data = [
        ["Name", "City"],
        ["Jarle", "Amsterdam"],
        ["Lisa", "Eindhoven"],
        ["Allex", "Eindhoven"],
    ]

    for row in data:
        worksheet.append(row)
    
    workbook.save("assignment.xlsx")

if __name__ == "__main__":
    create_excel()
