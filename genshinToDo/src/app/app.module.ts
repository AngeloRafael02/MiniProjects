import { NgModule } from '@angular/core';

import { BrowserModule } from '@angular/platform-browser';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AppRoutingModule,routingComponents } from './app-routing.module';

import { AppComponent } from './app.component';
import { ClockComponent } from './clock/clock.component';
import { TimerComponent } from './timer/timer.component';


@NgModule({
  declarations: [
    AppComponent,
    ClockComponent,
    TimerComponent,
    routingComponents
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
