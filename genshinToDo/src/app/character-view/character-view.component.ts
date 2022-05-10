import { Component, OnInit } from '@angular/core';
import { characterInterface } from '../interfaces';
import { MainService } from '../main.service';

@Component({
  selector: 'app-character-view',
  template: ` <p>CHARACTERS</p>
              <ul *ngFor="let Character of Characters">
                <li>{{Character.name}} : {{Character.element}} : {{Character.region}} : {{Character.domain}} : {{Character.availability}}</li>
              </ul>`,
  styles: [``]
})
export class CharacterViewComponent implements OnInit {

  public Characters:characterInterface[] = [];

  constructor(
    private _mainService:MainService
    ) { }

  ngOnInit(): void {
   this._mainService.getCharacterView()
    .subscribe(data => this.Characters = data);
  }

}
