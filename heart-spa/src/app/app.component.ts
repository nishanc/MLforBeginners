import { Component } from '@angular/core';
import { Data } from './models/data';
import { PredictionService } from './services/prediction.service';
import { Prediction } from './models/prediction';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Heart Attack Prediction';
  isPositive: boolean | undefined;
  constructor(private predictionService: PredictionService) { }

  onClickSubmit(data: Data) {
    this.predictionService.predict(data).subscribe(
    (res: Prediction) => {
      this.isPositive = (res.prediction == '1')
    },
    (error) => {
      alert('Error caught in component: \n' + error.message)
    });
  };

  reload(){
    window.location.reload();
  }
}
