import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-week-days',
  template: `
<nav>
  <ul>
      <li><a href="">Sunday</a></li>
      <li><a href="">Monday</a></li>
      <li><a href="">Tuesday</a></li>
      <li><a href="">Wednesday</a></li>
      <li><a href="">Thursday</a></li>
      <li><a href="">Friday</a></li>
      <li><a href="">Saturday</a></li>
  </ul>
</nav>`,
  styles: [`
  li {
    display: inline;
    margin-right: 1rem;
  }`]
})
export class WeekDaysComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
