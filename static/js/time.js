var RADIUS = 0.5,
    MarginTop = 0,
    MarfinLeft = 0,
    COLOR = '#000';
$(function () {
    var canvas = document.getElementById('canvas');
    canvas.width = '200';
    canvas.height = '35';
    var context = canvas.getContext('2d');

    setInterval(function () {
        var d = new Date();
        var h = d.getHours();
        var m = d.getMinutes();
        var s = d.getSeconds();
        canvas.height = canvas.height;
        render(context, h, m, s);
    }, 1000);
})

function render(cxt, h, m, s) {
    renderDigit(MarfinLeft, MarginTop, parseInt(h / 10), cxt)
    renderDigit(MarfinLeft + 15 * (RADIUS + 1), MarginTop, parseInt(h % 10), cxt)
    renderDigit(MarfinLeft + 30 * (RADIUS + 1), MarginTop, 10, cxt)
    renderDigit(MarfinLeft + 39 * (RADIUS + 1), MarginTop, parseInt(m / 10), cxt)
    renderDigit(MarfinLeft + 54 * (RADIUS + 1), MarginTop, parseInt(m % 10), cxt)
    renderDigit(MarfinLeft + 69 * (RADIUS + 1), MarginTop, 10, cxt)
    renderDigit(MarfinLeft + 78 * (RADIUS + 1), MarginTop, parseInt(s / 10), cxt)
    renderDigit(MarfinLeft + 93 * (RADIUS + 1), MarginTop, parseInt(s % 10), cxt)
}

function renderDigit(x, y, num, cxt) {
    cxt.fillStyle = COLOR;
    for (var i = 0; i < digit[num].length; i++) {
        for (var j = 0; j < digit[i].length; j++) {
            if (digit[num][i][j] == 1) {
                cxt.beginPath();
                cxt.arc(x + j * 2 * (RADIUS + 1) + (RADIUS + 1), y + i * 2 * (RADIUS + 1) + (RADIUS + 1), RADIUS, 0, 2 * Math.PI);
                cxt.closePath();
                cxt.fill();
            }
        }
    }

}
