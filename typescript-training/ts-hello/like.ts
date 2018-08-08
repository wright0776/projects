
// instantiate number of likes and if the user likes or not
// when user clicks like button, the button is highlighted and the number of likes 
// increases by 1
// if the user clicks the button again the button should be unselected and the 


export class Like {
    constructor(public likes: number, public clientLikes: boolean) {}

    clientClick() {
        if (this.clientLikes === false) {
            this.likes++;
            this.clientLikes = true;
            console.log(this.likes);
        } else {
            this.likes--;
            this.clientLikes = false;
            console.log(this.likes);
        }
    }
}