const main = document.getElementById('main');

// adds an element, parameter taken is an object with tag, cl (class), id, cont (text node content), and parent element to be appended to //

const addElement = (obj) => {
    const el = document.createElement(obj.tag);
    el.className = obj.cl;
    el.id = obj.id;
    if(obj.cont){
        const tn = document.createTextNode(obj.cont);
        el.appendChild(tn);
    }
    el.draggable = true;
    obj.parent.appendChild(el);
}

// Creates blue button, appends to div "main" //

const blueButton = () => {
    const button = document.createElement("button");
    button.className = "blueButton";
    button.id = "blueButton";
    const tn = document.createTextNode("blue button");
    button.appendChild(tn);
    main.appendChild(button);
}

blueButton();

// constructs an object for addElement function //

class ElementObj {
    constructor(tag,cl,id,cont,parent) {
        this.tag = tag;
        this.cl = cl;
        this.id = id;
        this.cont = cont;
        this.parent = parent;
    }
}

// create object for circleContainer div
const circleContainerObj = new ElementObj("div","circleContainer","circleContainer","",main);

// create circleContainer div
addElement(circleContainerObj);

// get circleContainer div
const circleContainer = document.getElementById("circleContainer");

// create object for redCircle div
const redCircleObj = new ElementObj("div","redCircle","redCircle","red circle",circleContainer);

let mainButton = document.getElementById("blueButton");
mainButton.addEventListener("click", ()=>addElement(redCircleObj));