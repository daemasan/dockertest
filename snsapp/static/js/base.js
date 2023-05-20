document.addEventListener('DOMContentLoaded', function(){
    const getCookie = (name) => {
        if (document.cookie && document.cookie !== '') {
            for (const cookie of document.cookie.split(';')) {
                const [key, value] = cookie.trim().split('=');
                if (key === name) {
                    return decodeURIComponent(value);
                }
            }
        }
    };
    const csrftoken = getCookie('csrftoken');
    const test = document.getElementById('test');
        /*
    const topdf = document.getElementById('topdf');

    topdf.addEventListener('click',(event) => {
        //form = new FormData(document.forms[1]);
        printpdf();
    })
    
    async function printpdf(){
        let response = await fetch("to_pdf/",{method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },      
        })
        .then((response) => response.blob())
        .then((myBlob) => {
            
            const objectURL = URL.createObjectURL(myBlob);
            console.log(myBlob)
            window.open(objectURL)
        })
    }
    */
    console.log('open')
    const detaillink = document.getElementsByClassName('detaillink');
    for(let i = 0; i < detaillink.length; i++) {
        detaillink[i].addEventListener('click', (event) => {
            event.preventDefault;
            testlink()
   
        });
    }
    async function testlink(){
        console.log('open')
        open()
    }
});
