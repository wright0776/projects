"use strict";
// instantiate number of likes and if the user likes or not
// when user clicks like button, the button is highlighted and the number of likes 
// increases by 1
// if the user clicks the button again the button should be unselected and the 
exports.__esModule = true;
var Like = /** @class */ (function () {
    function Like(likes, clientLikes) {
        this.likes = likes;
        this.clientLikes = clientLikes;
    }
    Like.prototype.clientClick = function () {
        if (this.clientLikes === false) {
            this.likes++;
            this.clientLikes = true;
            console.log(this.likes);
        }
        else {
            this.likes--;
            this.clientLikes = false;
            console.log(this.likes);
        }
    };
    return Like;
}());
exports.Like = Like;
