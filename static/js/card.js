const speech = new webkitSpeechRecognition();
speech.lang = 'ja-JP';

const spbtn_1 = document.getElementById('speechbutton_1');
const spbtn_2 = document.getElementById('speechbutton_2');
const spbtn_3 = document.getElementById('speechbutton_3');
const spbtn_4 = document.getElementById('speechbutton_4');
const spbtn_5 = document.getElementById('speechbutton_5');
const spbtn_6 = document.getElementById('speechbutton_6');

const recstart = () => {
    speech.start();
}
if (spbtn_1 !=null){
    spbtn_1.addEventListener('click', recstart);
} if (spbtn_2 != null){
    spbtn_2.addEventListener('click', recstart);
} if (spbtn_3 != null){
    spbtn_3.addEventListener('click', recstart);
} if (spbtn_4 !=null){
    spbtn_4.addEventListener('click', recstart);
} if (spbtn_5 != null) {
    spbtn_5.addEventListener('click', recstart);
} if (spbtn_6 != null) {
    spbtn_6.addEventListener('click', recstart);
};


speech.addEventListener('result', function (e) {
    console.log(e)
    // 音声認識で取得した情報を、コンソール画面に表示
    if (id_title.value == "") {
        id_title.value = e.results[0][0].transcript;
    } else if (id_subtitle.value == "") {
        id_subtitle.value = e.results[0][0].transcript;
    } else if (id_content.value == "") {
        id_content.value = e.results[0][0].transcript;
    } else if (id_what.value == "") {
        id_what.value = e.results[0][0].transcript;
    } else if (id_why.value == "") {
        id_why.value = e.results[0][0].transcript;
    } else {
        id_sowhat.value = e.results[0][0].transcript;
    };
});