import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-username-input',
  templateUrl: './username-input.component.html',
  styleUrls: ['./username-input.component.css']
})
export class UsernameInputComponent implements OnInit {
  username = '';
  // allowSubmit = false;

  constructor() { }

  ngOnInit() {
  }

  // onUpdateUsername(event) {
  //   this.username = (<HTMLInputElement>event.target).value;
  //   if (this.username.length > 0) {
  //     this.allowSubmit = true;
  //   } else {
  //     this.allowSubmit = false;
  //   }
  // }

  // onSubmitUsername() {
  //   this.username = '';
  //   this.allowSubmit = false;
  // }

}
