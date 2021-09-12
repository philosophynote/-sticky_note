
const startScanner = () =>{
    Quagga.init({
        inputStream: {
            name: "Live",
            type: "LiveStream",
            target: document.querySelector('#photo-area'),
            constraints: {
                decodeBarCodeRate: 3,
                successTimeout: 500,
                codeRepetition: true,
                tryVertical: true,
                frameRate: 15,
                width: 640,
                height: 480,
                facingMode: "environment"
            },
        },
        decoder: {
            readers: [
                "ean_reader"
            ]
        },

    }, function (err) {
        if (err) {
            console.log(err);
            return
        }

        console.log("Initialization finished. Ready to start");
        Quagga.start();

        // Set flag to is running
        _scannerIsRunning = true;
    });

    Quagga.onProcessed(function (result) {
        var drawingCtx = Quagga.canvas.ctx.overlay,
            drawingCanvas = Quagga.canvas.dom.overlay;

        if (result) {
            if (result.boxes) {
                drawingCtx.clearRect(0, 0, parseInt(drawingCanvas.getAttribute("width")), parseInt(drawingCanvas.getAttribute("height")));
                result.boxes.filter(function (box) {
                    return box !== result.box;
                }).forEach(function (box) {
                    Quagga.ImageDebug.drawPath(box, {
                        x: 0,
                        y: 1
                    }, drawingCtx, {
                        color: "green",
                        lineWidth: 2
                    });
                });
            }

            if (result.box) {
                Quagga.ImageDebug.drawPath(result.box, {
                    x: 0,
                    y: 1
                }, drawingCtx, {
                    color: "#00F",
                    lineWidth: 2
                });
            }

            if (result.codeResult && result.codeResult.code) {
                Quagga.ImageDebug.drawPath(result.line, {
                    x: 'x',
                    y: 'y'
                }, drawingCtx, {
                    color: 'red',
                    lineWidth: 3
                });
            }
        }
    });


    //barcode read call back
    Quagga.onDetected(success => {
        const code =success.codeResult.code;
        if(calc(code))
            console.log(code);
            document.getElementById("q").value=code

    });
    
}


const calc = (isbn) =>{
    const arrlsbn = isbn.toString().split("").map(num => parseInt(num));
    let remainder = 0;
    const checkDigit = arrlsbn.pop();

    arrlsbn.forEach((num,index)=>{
        remainder += num*(index % 2 === 0?1:3);
    });
    remainder %= 10;
    remainder = remainder ===0?0 : 10 -remainder;

    return checkDigit ===remainder;
}

    //検索する

//本を検索して結果を返す
const searchBooks=async (query) => {
    //Google Books APIs のエンドポイント
    let endpoint = 'https://www.googleapis.com/books/v1';
    console.log(query)
    let res = await fetch(`${endpoint}/volumes?q=${query}`);

    let data = await res.json();
    console.log(data)
    let items = data.items.map(item => {
        let vi = item.volumeInfo;
        return {
            title: vi.title,
            descrition: vi.description,
            link: vi.infoLink,
            image: vi.imageLinks ? vi.imageLinks.smallThumbnail : '',
        };
    });

    return items;
};

const search = async () => {
    //入力された値で本を検索
    let books = $("#q").val()
    let items = await searchBooks(books);
    //map関数は配列の各要素に対して処理を実行する
    let texts = 
            `<div>
                <img class='w100 object-fit-contain bg-gray' src='${items[0].image}' />
                <div class='p16'>
                    <h3 class='mb8'>${items[0].title}</h3>
                    <p class='line-clamp-2'>${items[0].descrition}</p>
                </div>
                <button type="button" class="btn btn-success ISBNsave" data-mdb-target="#updateModal" data-mdb-toggle="modal" data-mdb -dismiss="modal">選択</button>
                <br>
            </div>`;
    ;
    document.getElementById("results").innerHTML= texts;
    return items[0]
};

//選択された本をフォーム欄に登録する
const Booksave =async () =>{
    const book = await search()
    console.log(book)
    let book_title = book.title;
    let book_descrition = book.descrition;
    document.getElementById("id_title").value = book_title
    document.getElementById("id_subtitle").value = book_descrition
}

$("#ISBNbutton").on("click", startScanner);
$("#readbook").on("click", search);
$(document).on("click",".ISBNsave",Booksave)

//
//