let MovieObject = {
    init: function(){
        alert("init함수가 불려짐")
    },

    getall: function(){
       alert("getall  함수가 불려짐")
       $.ajax({
       // 실행할 코드
          type: "GET",
          url: "http://localhost:8000/all",
       }).done(function(response){
       // 성공코드
            console.log(response)
            movielist = response.result

            topdiv = document.createElement("div")
            document.body.appendChild(topdiv)

            // 첫번째 영화이미지
            cmovie = document.createElement("div")
            cmovie.className = "card"

            mimg = document.createElement("img")
            mimg.className = "card-img-top"
            mimg.src = movielist[0].poster_path
            cmovie.appendChild(mimg)
            topdiv.appendChild(cmovie)

            //두번째영화이미지
            cmovie = document.createElement("div")
            cmovie.className = "card"

            mimg = document.createElement("img")
            mimg.className = "card-img-top"
            mimg.src = movielist[1].poster_path
            cmovie.appendChild(mimg)
            topdiv.appendChild(cmovie)

       }).fail(function(error){
           // 실패코드
           console.log(error)
       });
    }
}

MovieObject.init();
MovieObject.getall();