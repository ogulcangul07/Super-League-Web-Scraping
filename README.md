# Super-League-Web-Scraping
A Python-based web scraping tool for scraping Super League Players data such as player information, market values, teams and values from Transfermarkt.

## 📌 Features
- Scrape player details (name, position, nationality, etc.)
- Extract market value and transfer history
- Export results to CSV
- Track total execution time
- Lightweight and easy to modify

## 🛠️ Technologies Used
- **Python 3**
- [requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [pandas](https://pandas.pydata.org/)
- [re](https://docs.python.org/3/library/re.html)
- [time](https://docs.python.org/3/library/time.html)

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ogulcangul07/Super-League-Web-Scraping.git
   cd Super-League-Web-Scraping


   
The generated CSV file contains the following columns:
| Column Name         | Description |
|---------------------|-------------|
| **Player**          | Full name of the player |
| **Number**          | Player's squad number (if available) |
| **Position**        | Playing position (e.g., Forward, Midfielder, Defender, Goalkeeper) |
| **Team**            | Name of the team |
| **Age**             | Player's age |
| **Country**         | Player's primary nationality |
| **Height**          | Player's height (in meters) |
| **Foot**            | Preferred foot (Left, Right, or Both) |
| **Value**           | Current market value of the player (in EUR) |
| **Previous Team**   | Name of the previous club before joining |
| **TransferFee**     | Transfer fee paid (if available) |
| **Status**          | Contract type with the current club (Permanent or Loan) |

> **Disclaimer**  
> This project is for **educational and personal use only**.  
> All data scraped belongs to **Transfermarkt**.  
> This project has **no commercial purpose**.
