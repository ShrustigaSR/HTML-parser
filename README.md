# HTML to JSON Parser with Flask

This is a simple web application built with Flask that allows you to upload an HTML file, parse it, and convert the parsed data into a JSON format.

## Dependencies

- Flask
- BeautifulSoup (bs4)
- Werkzeug

## File Structure

- `app.py`: The Flask application file.
- `templates/`: Folder containing HTML template.
- `input/`: Folder where sample html files are stored.
- `output/`: Folder where respective output files of the sample HTML files are stored.


## Installation
1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:
     ```bash
     venv\Scripts\activate
     ```

3. Install the dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

   The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Output

#### No file chosen
![image](https://github.com/ShrustigaSR/HTML-parser/assets/53357626/a2922c94-862c-40ef-8267-879f65b02c94)

#### File other than HTML is uploaded
![image](https://github.com/ShrustigaSR/HTML-parser/assets/53357626/6f43ea97-058e-4576-91ea-1d9f6184fb78)








