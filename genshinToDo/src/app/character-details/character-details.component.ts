import { Component, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { characterInterface } from '../interfaces';
import { MainService } from '../main.service';

@Component({
  selector: 'app-character-details',
  template: `
  <button (click)="prev()">PREV</button> <button (click)="back()">BACK</button> <button (click)="next()">NEXT</button>
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
    private router:Router,
  ) { }

  ngOnInit(): void {
    this.charNumber = this.route.snapshot.params['id']

    this._mainService.getCharacterView()
    .subscribe(data => this.content = data);

    this.route.paramMap.subscribe((params:any)=>{
      let id = parseInt(params.get('id'));
      this.charNumber = id;
    });
  }
  
  prev(){
    let prevId:number = this.charNumber - 1;
    if (prevId < 0) { prevId = 0; }
    this.router.navigate(['/Characters',prevId])
  }
  back(){
    this.router.navigate(['/Characters']);
  }
  next(){
    let nextId:number = this.charNumber + 1;
    this.router.navigate(["/Characters",nextId])
  }
}
