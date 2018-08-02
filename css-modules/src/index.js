// require('./alert.js');
// import greetings from './robot.js';
// document.write(greetings("Hello", "Matt"));

import styles from './app.css';

let element =
    `<div class="${styles.element}">
        <p>And the blue cat jumped over the moon.</p>
    </div>`
console.log(styles.element)
document.write(element);