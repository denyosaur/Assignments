/** Given a query string, return array of matching shows:
 *     { id, name, summary, episodesUrl }
 */


/** Search Shows
 *    - given a search term, search for tv shows that
 *      match that query.  The function is async show it
 *       will be returning a promise.
 *
 *   - Returns an array of objects. Each object should include
 *     following show information:
 *    {
        id: <show id>,
        name: <show name>,
        summary: <show summary>,
        image: <an image from the show data, or a default imege if no image exists, (image isn't needed until later)>
      }
 */
async function searchShows(query) {
  // TODO: Make an ajax request to the searchShows api.  Remove
  // hard coded data.
  const res = await axios.get("http://api.tvmaze.com/search/shows", { params: { q: query } })
  let showArr = [];
  for (let data of res.data) {
    const resImages = await axios.get(`http://api.tvmaze.com/shows/${data.show.id}/images`)
    showArr.push({
      id: data.show.id,
      name: data.show.name,
      summary: data.show.summary,
      image: resImages.data[0].resolutions.original
    });
  }
  return showArr;
}



/** Populate shows list:
*     - given list of shows, add shows to DOM
*/

function populateShows(shows) {
  const $showsList = $("#shows-list");
  $showsList.empty();

  for (let show of shows) {
    let showImg = show.image.url !== null ? show.image.url : "https://tinyurl.com/tv-missing";
    let $item = $(
      `<div class="col-md-6 col-lg-3 Show" data-show-id="${show.id}">
          <div class="card" data-show-id="${show.id}">
            <img class="card-img-top" src="${showImg}">
            <div class="card-body">
              <h5 class="card-title">${show.name}</h5>
              <p class="card-text">${show.summary}</p>
            </div>
            <input type="button" class="eListBtn" value="Episode List">
            <div class="eListDiv"> </div>
          </div>
        </div>
      `);
    $showsList.append($item);

  }
}

//Click event listener for episode list button
$("#shows-list").on("click", ".eListBtn", async function (evt) {
  evt.preventDefault();
  $("ul").empty();
  let showId = $(evt.target).closest(".Show").data("show-id");
  let episodes = await getEpisodes(showId);
  listEpisodes(episodes);
})
//button to add episode list to cards


/** Handle search form submission:
 *    - hide episodes area
 *    - get list of matching shows and show in shows list
 */

$("#search-form").on("submit", async function handleSearch(evt) {
  evt.preventDefault();

  let query = $("#search-query").val();
  if (!query) return;

  $("#episodes-area").hide();

  let shows = await searchShows(query);

  populateShows(shows);

});




/** Given a show ID, return list of episodes:
 *      {id, name, season, number}
 */

async function getEpisodes(id) {
  // TODO: get episodes from tvmaze
  //       you can get this by making GET request to
  //       http://api.tvmaze.com/shows/SHOW-ID-HERE/episodes

  const episodeList = await axios.get(`http://api.tvmaze.com/shows/${id}/episodes`);
  let episodes = episodeList.data.map(episode => ({
    id: episode.id,
    name: episode.name,
    season: episode.season,
    number: episode.number,
  }));
  return episodes;
  // TODO: return array-of-episode-info, as described in docstring above
}

//list episodes information in an LI and append to the UL
function listEpisodes(episodes) {
  for (let episode of episodes) {
    let $episode = $(
      `<li>
        ${episode.id}: ${episode.name}, episode #${episode.number}, season ${episode.season}
      </li>`
    );
    $("ul").append($episode);
  }
  $("#episodes-area").show()
}