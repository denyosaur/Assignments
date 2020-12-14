const searchInput = document.getElementById("userInput");
const searchBtn = document.querySelector("#searchButton");
const removeBtn = document.getElementById("removeButton");

//Search button event listener. Takes the text that user inputs and runs the getPicture function.
$("#searchButton").on("click", function (evt) {
    evt.preventDefault();
    let searchText = searchInput.value;
    getPicture(searchText);
})
//Remove button event listener. Removes all img tags under #pictureResults
$("#removeButton").on("click", function (evt) {
    evt.preventDefault();
    $("#pictureResults").remove(".gif")
})

// this function takes the search text and sends a request to API along with key
async function getPicture(search) {
    //Connect with API and get data object
    let res = await axios.get("https://api.giphy.com/v1/gifs/search", {
        params: {
            api_key: "UEvD3v0YkGKD59CquSc1Jamx0wRCaTbx",
            q: `${search}`
        }
    })
    let results = res.data.data;
    let randomIndex = Math.floor(Math.random() * results.length);
    let randomPictureUrl = results[randomIndex].images.original.url;
    createPicture(randomPictureUrl);
}

//function to append image to div. To be executed in getPicture()
function createPicture(pictureLink) {
    let img = $("<img>");
    img.attr({ src: `${pictureLink}`, class: "gif" });
    img.appendTo("#pictureResults");
}



