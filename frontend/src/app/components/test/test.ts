import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.html'
})
export class TestComponent implements OnInit {

  message: string = 'Loading...';

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.getTest().subscribe({
      next: (res: any) => {
        this.message = res.message;
      },
      error: () => {
        this.message = 'Error connecting to backend';
      }
    });
  }
}