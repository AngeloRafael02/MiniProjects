import { Component, OnInit } from '@angular/core';
import { characterInterface } from '../interfaces';
import { MainService } from '../main.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-character-view',
  template: ` <p>CHARACTERS</p>
              <ul class="chars" *ngFor="let Character of Characters">
              <span class="item">
                <li (click)="onSelect(Character)">{{Character.name}}</li>
              </span>
                </ul>`,
  styles: [``]
})
export class CharacterViewComponent implements OnInit {

  public Characters:characterInterface[] = [];

  constructor(
    private _mainService:MainService,
    private router:Router
    ) { }

  ngOnInit(): void {
   //service
   this._mainService.getCharacterView()
    .subscribe(data => this.Characters = data);
  }

  onSelect(Character:any){
    this.router.navigate(['/Characters', Character.id]);
  }
}
