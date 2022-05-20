import { Component, OnInit } from '@angular/core';
import { characterInterface } from '../interfaces';
import { MainService } from '../main.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-character-view',
  template: ` 
  <p>CHARACTERS</p>
    <ul class="chars justify-content-center" *ngFor="let Character of Characters">
      <abbr title="{{Character.name}}">
      <img src="{{Character.imgURL}}" alt="{{Character.name}}" (click)="onSelect(Character)" [class.selected]="wasSelected(Character)">
      </abbr>
    </ul>
  `,
  styles: [`
  img { width:7.5%; }
  img:hover { border-style: solid; border-color:grey; }
  img.selected{ border-style: solid; border-color:black; }
  `]
})
export class CharacterViewComponent implements OnInit {

  public Characters:characterInterface[] = [];
  public selectedId:number = 0;
  
  constructor(
    private _mainService:MainService,
    private route:ActivatedRoute,
    private router:Router
    ) { }

  ngOnInit(): void {
   //service: subscribe to the function calling Character Data
   this._mainService.getCharacterView()
    .subscribe(data => this.Characters = data);

  //gets id from URL using optional Route Parameters(using the URL as a variable/argument)
    this.route.paramMap.subscribe((params:any)=>{
      let id = parseInt(params.get('id'));
      this.selectedId = id;
    });
  }

  onSelect(Character:characterInterface):void{ //navigates to a route according to the id number of the character
    this.router.navigate(['/Characters', Character.id]);
  }

  wasSelected(Character:any):boolean{ //return true item was selected, procs a class bind of css styles
    return Character.id === this.selectedId
  }
}
