package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;


public class MainActivity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        //setText
        String message = getIntent().getStringExtra("message");
        String processedMessage = message.toUpperCase();
        TextView textView = (TextView) findViewById(R.id.textView2);
        textView.setText(processedMessage);
        //pass data to Mainactivity
        Button button = (Button)findViewById(R.id.button2);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity2.this, MainActivity.class);
                intent.putExtra("result", processedMessage);
                setResult(Activity.RESULT_OK, intent);
                finish();
            }
        });
    }
}
