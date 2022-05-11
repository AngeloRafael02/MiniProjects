import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { characterInterface } from '../interfaces';
import { MainService } from '../main.service';

@Component({
  selector: 'app-character-details',
  template: `
    <p> Name: {{ content[charNumber].name }}
      {{ content[charNumber].region }}
    </p>
  `,
  styles: [
  ]
})
export class CharacterDetailsComponent implements OnInit {

  public content:characterInterface[] = [];
  public charNumber:number = 0;

  constructor(
    private _mainService:MainService,
    private route:ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.charNumber = this.route.snapshot.params['id']

    this._mainService.getCharacterView()
    .subscribe(data => this.content = data);
  }

}
