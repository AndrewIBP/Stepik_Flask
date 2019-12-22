from flask import Flask, render_template  # сперва подключим модуль
import data

app = Flask(__name__)  # объявим экземпляр фласка


@app.route('/')
def main():
    return render_template('index.html', title=data.title, subt=data.subtitle, desc=data.description, direction=data.departures, tours=data.tours)


@app.route('/from/<directions>/')
def direction(directions):
    tour_from = {}
    for key in data.tours:  #выбираем туры которые соответствуют направлению
        if data.tours[key]["departure"] == directions:
            tour_from = data.tours[key]
    return render_template('direction.html', title=data.title, direct=data.departures[directions], direction=data.departures, tours=tour_from)


@app.route('/tours/<int:ids>/')
def tours(ids):
    return render_template('tour.html', title=data.title, direction=data.departures, tours=data.tours[ids])


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что-то не так, но мы все починим"


if __name__ == '__main__':
    app.run(debug=True)
