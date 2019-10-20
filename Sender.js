/**
 * Created by on 10/20/19.
 */

var i = 0;
function sendData() {

    i++;
    process.stdout.write((100 + i) + '\n');

    if (i < 5) {
        setTimeout(sendData, 2000);
    } else {
        throw new Error();
    }
}

sendData();