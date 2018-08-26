import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-display-details',
  templateUrl: './display-details.component.html',
  styleUrls: ['./display-details.component.css']
})
export class DisplayDetailsComponent implements OnInit {
  detailsDisplayed = false;
  clicks = 0;
  timestamps = [];

  constructor() { }

  ngOnInit() {
  }

  onDisplayDetails() {
    this.detailsDisplayed = !this.detailsDisplayed;
    this.clicks++;
    this.timestamps.push(new Date().toString());
  }

}
