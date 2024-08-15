import requests
import pandas as pd
from fpdf import FPDF
from bs4 import BeautifulSoup

# Function to fetch data from API or scrape from website
def fetch_data(url):
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")  # Debugging: Check status code
    if response.status_code == 200:
        try:
            # If the data is in JSON format
            data = response.json()
            print(f"Data fetched (JSON): {data}")  # Debugging: Print data
            return data
        except ValueError:
            # If the data is not in JSON format, try to scrape it
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"Data fetched (HTML): {soup.prettify()}")  # Debugging: Print HTML
            # Parse the data from the HTML as needed
            # This part needs to be customized based on the website structure
            data = []
            for item in soup.find_all('div', class_='data-item'):
                data.append({
                    'field1': item.find('span', class_='field1').text,
                    'field2': item.find('span', class_='field2').text,
                    # Add more fields as needed
                })
            return data
    else:
        print(f"Failed to fetch data: {response.status_code}")  # Debugging: Error message
        return None

# Function to save data to an Excel file
def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

# Function to save data to a PDF file
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Company Data', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def save_to_pdf(data, filename):
    pdf = PDF()
    pdf.add_page()
    for item in data:
        for key, value in item.items():
            pdf.chapter_title(f'{key}:')
            pdf.chapter_body(f'{value}')
    pdf.output(filename)

# Main function
def main():
    url = 'https://smarterp.top/'  # Replace with your API endpoint or website URL
    data = fetch_data(url)

    if data:
        save_to_excel(data, 'company_data.xlsx')
        save_to_pdf(data, 'company_data.pdf')
        print('Data successfully saved to company_data.xlsx and company_data.pdf')
    else:
        print('No data found.')

if __name__ == '__main__':
    main()
