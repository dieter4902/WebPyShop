{
    "use strict"
    let rating = document.getElementById("id_rating")
    if (rating) {
        let stars = document.getElementsByClassName("fa-star");
        const numStars = stars.length;
        for (let i = 0; i < numStars; i++) {
            stars[i].addEventListener('click', function () {
                for (let x = 0; x < numStars; x++) {
                    if (x <= i) {
                        stars[x].classList.add("checked")
                    } else {
                        stars[x].classList.remove("checked")
                    }
                }
                rating.value = i + 1
            });
        }
        rating.hidden = true
    }
}