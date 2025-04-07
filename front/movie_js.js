let MovieObject = {
    init: function(){

    },

    getall: function(){

       $.ajax({
       // 실행할 코드
          type: "GET",
          url: "http://localhost:8000/all",
       }).done(function(response){
       // 성공코드
            console.log(response)
            movielist = response.result

            // topdiv = document.createElement("div")
            // topdiv.style = "column-count:5"
            // document.body.appendChild(topdiv)
            topdiv = document.getElementById("alldiv")

            movielist.forEach( movie => {
                cmovie = document.createElement("div")
                cmovie.className = "card"
    
                mimg = document.createElement("img")
                mimg.className = "card-img-top"
                mimg.src = movie.poster_path
                mimg.onclick = function(){
                    // location.href = movie.url  // 현재창에서 열기
                    window.open(movie.url)  // 새창에서 열기
                }
                mimg.onmouseover = function(){
                    
                }
                mimg.style.cursor = "pointer"
                cmovie.appendChild(mimg)
                topdiv.appendChild(cmovie)
            });       
       }).fail(function(error){
           // 실패코드
           console.log(error)
       });
    },


    getgenres: function(){

        genre = document.getElementById("sgenre").value.toLowerCase()

        $.ajax({
        // 실행할 코드
           type: "GET",
           url: "http://localhost:8000/genresbest/" + genre,
        }).done(function(response){
        // 성공코드
             console.log(response)
             movielist = response.result
 
             topdiv = document.getElementById("genrediv")
            //  topdiv.innerHTML = ""  // 기존영화내용을 없애는 첫번째 방법
            // 두번째 방법법
            while(topdiv.firstChild){
                topdiv.removeChild(topdiv.firstChild)
            }
 
             movielist.forEach( movie => {
                 cmovie = document.createElement("div")
                 cmovie.className = "card"
     
                 mimg = document.createElement("img")
                 mimg.className = "card-img-top"
                 mimg.src = movie.poster_path
                 mimg.onclick = function(){
                     // location.href = movie.url  // 현재창에서 열기
                     window.open(movie.url)  // 새창에서 열기
                 }
                 mimg.onmouseover = function(){
                     
                 }
                 mimg.style.cursor = "pointer"
                 cmovie.appendChild(mimg)
                 topdiv.appendChild(cmovie)
             });       
        }).fail(function(error){
            // 실패코드
            console.log(error)
        });
     }
}

MovieObject.init();
MovieObject.getall();