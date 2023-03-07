package com.example.myapplication;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.media.Image;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    EditText editText;
    ImageView imageView;
    Button  button;

    private ActivityResultLauncher<Intent> activityResultLauncher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(), new ActivityResultCallback<ActivityResult>() {
        @Override
        public void onActivityResult(ActivityResult result) {
            if(result.getResultCode() == RESULT_OK){
                Intent intent = result.getData();
                String strResult = intent.getStringExtra("result");
                textView.setText(strResult);
            }
        }
    });

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initUI();
        setUI();
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.d("OnCreate", "Click button");
                String message = editText.getText().toString().trim();
                onClickGoToSecondActivity(message);
            }
        });
    }

    private void onClickGoToSecondActivity(String message) {
        Intent intent = new Intent(MainActivity.this, MainActivity2.class);
        intent.putExtra("message", message);
        activityResultLauncher.launch(intent);
    }

    private void initUI(){
        editText = findViewById(R.id.editText);
        textView = findViewById(R.id.textView);
        imageView = findViewById(R.id.imageView);
        button = findViewById(R.id.button);
    }

    private void setUI(){
        textView.setText(R.string.hello);
        imageView.setImageResource(R.drawable.splash);
    }
}
