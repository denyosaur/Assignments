class Jeopardy {
    constructor() {
        this.height = 6;
        this.width = 6;
        this.categories = [];
        this.showLoadingView();
        this.makeHtmlBoard();
        this.setupAndStart();
    };

    //make HTML skeleton for the game board
    makeHtmlBoard() {
        $("#startBtnDiv").after(`
        <div id="gameBoard">
            <table id="questionTable">
                <thead>
                    <tr id="topRow">
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </div>
    `);
    };

    // remove #gameBoard and all children to reset board. show loading gif, 
    //and disable button to prevent multiple requests at once
    showLoadingView() {
        $("#gameBoard").remove();
        $("#loadingGif").show();
        $("#startBtn").prop("disabled", true);
    }

    async setupAndStart() {
        //push the category data into an array
        //set up the HTML board with the categories
        let catArr = this.getCategoryIDs();
        for (let catId of catArr) {
            const categoryData = {};
            const clues = [];
            const res = await axios.get("http://jservice.io/api/clues", { params: { category: `${catId}` } });
            //push in title of the category into the Category object
            categoryData["title"] = res.data[0].category.title;

            //use randomQuestionNum() to pull in an array of random numbers according to the number of questions that
            //are available for this category. Then use the numbers in the array as an index to pull in questions and
            //clues. 
            const randomArray = this.randomQuestionNum(res.data.length);
            for (let questionIdx of randomArray) {
                clues.push(this.getCategory(res.data[questionIdx]));
            }
            //Push those questions and clues into temporary clues array, then push into the Categories array
            categoryData["clues"] = clues;
            this.categories.push(categoryData);
        }
        this.fillTable(this.categories);
        this.hideLoadingView();

    }

    //change the button to say "restart", hide the loading GIF, and re-enable the start/restart button
    hideLoadingView() {
        $("#startBtn").val("Restart");
        $("#loadingGif").hide();
        $("#startBtn").prop("disabled", false);
    }

    // take in the data from API and return an object of only the question, answer, and showing info
    getCategory(catId) {
        return {
            question: catId.question,
            answer: catId.answer,
            showing: null
        };

    };

    //select 6 random numbers ranging from 0 to 18,412 (this is the total number of categories), and return as an array
    // this is used to select 6 topics randomly
    getCategoryIDs(data) {
        let categoryIds = [];
        while (categoryIds.length < this.width) {
            let randomNum = Math.floor(Math.random() * 18412);
            if (categoryIds.indexOf(randomNum) === -1) {
                categoryIds.push(randomNum);
            };
        };
        return categoryIds;
    };

    // fill out the HTML table with the game data, including question and answer
    fillTable(data) {
        const $topicRow = $("#topRow");
        for (let category of data) {
            let categoryTitle = $(`<th>${category.title}</th>`);
            $topicRow.append(categoryTitle);
        };
        //This foor loop iterates through each row and has a nested loop within to iterate through each topic 
        //separately. Once the for loop nested below completes, it appends the completed row to $("tbody").
        //This also adds in a class for whether the boxes were clicked on.
        for (let rowX = 0; rowX < 5; rowX++) {
            const $newRow = $("<tr></tr>");
            //The for loop below creates the question boxes one column at a time. It pulls in data for each topic 
            // and creates a box in the corresponding row.
            for (let colY = 0; colY < 6; colY++) {
                $($newRow).append(`
                    <td class="${colY},${rowX}">
                        <span class= "questionMark"> $${(rowX + 1) * 2}00</span >
                        <span class="question">${data[colY].clues[rowX].question}</span>
                        <span class="answer">${data[colY].clues[rowX].answer}</span>
                    </td >
                `);
            }
            $("tbody").append($newRow);
            $("span").hide();
            $(".questionMark").show();
        }
        this.handleClick();
    };

    //function for handling clicks on each TD square
    handleClick() {
        let cats = this.categories;
        //add the event listener function on each of the TDs
        $("td").each(function () {
            $(this).on("click", function (evt) {
                const target = evt.currentTarget;
                //below variable takes the class from the TD elements, splits them into an array of integers
                let status = $(this).attr("class").split(",").map(Number);
                // "cats[status[0]].clues[status[1]].showing" is the "showing" status in the categories object
                // if the .showing is null, update it to "showing".
                // Then hide all spans, but only show the spans with class of .question
                //
                // if the .showing is "showing", then update the property to "answer"
                // Then hide all spans, but only show the spans with class of .answer
                if (cats[status[0]].clues[status[1]].showing === null) {
                    cats[status[0]].clues[status[1]].showing = "showing";
                    $(target).closest("td").children("span").hide();
                    $(target).closest("td").children(".question").show();
                } else if (cats[status[0]].clues[status[1]].showing === "showing") {
                    cats[status[0]].clues[status[1]].showing = "answer";
                    $(target).closest("td").children("span").hide();
                    $(target).closest("td").children(".answer").show();
                };
            });
        });
    };

    // randomQuestionNum() is used to get an array of random numbers according to the number of questions in a given topic.
    // this is used to randomly pick 5 questions out of a topic, if the topic has more than 5 questions available
    randomQuestionNum(num) {
        let randomNum = [];
        while (randomNum.length < this.height - 1) {
            let randomIdx = Math.floor(Math.random() * num);
            if (randomNum.indexOf(randomIdx) === -1) {
                randomNum.push(randomIdx);
            };
        }
        return randomNum;
    };
};



// once the document is ready, create a start button and set up the html skeleton for the table
$(document).ready(createButton => {
    $("body").prepend(`
    <div id="startBtnDiv">
        <input type="button" id="startBtn" value="Start">
    </div>
    <div id="loadingGif">
        <img src="https://i.imgur.com/K6hmwpS.gif" id="loading">
    </div>
    `)
    $("#loadingGif").hide();
});

//event listener added on to start button. this executes the Jeopardy class
$("body").on("click", "#startBtn", function (evt) {
    evt.preventDefault();
    new Jeopardy().then(hideLoadingView());
});


// I could not get this to work.
// $(document).ajaxStart(function () {
//     $("#loading").show();

// }).ajaxStop(function () {
//     $("#loading").hide();
// });