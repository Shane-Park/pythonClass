package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame08 extends JFrame {

	private JPanel contentPane;
	private JTextField tfCom;
	private JTextField tfMine;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame08 frame = new MyFrame08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 248, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("내 선택");
		lblNewLabel.setBounds(21, 77, 61, 16);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("컴퓨터");
		lblNewLabel_1.setBounds(21, 105, 61, 16);
		contentPane.add(lblNewLabel_1);
		
		tfCom = new JTextField();
		tfCom.setBounds(94, 100, 130, 26);
		contentPane.add(tfCom);
		tfCom.setColumns(10);
		
		tfMine = new JTextField();
		tfMine.setBounds(94, 67, 130, 26);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		JButton btn = new JButton("결과보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				getResult();
			}
		});
		btn.setBounds(21, 151, 203, 29);
		contentPane.add(btn);
		
		JLabel lblNewLabel_2 = new JLabel("결과");
		lblNewLabel_2.setBounds(21, 210, 61, 16);
		contentPane.add(lblNewLabel_2);
		
		tfResult = new JTextField();
		tfResult.setBounds(94, 205, 130, 26);
		contentPane.add(tfResult);
		tfResult.setColumns(10);
		
		JLabel lblNewLabel_3 = new JLabel("가위바위보 게임하기");
		lblNewLabel_3.setBounds(21, 17, 115, 16);
		contentPane.add(lblNewLabel_3);
		
		JButton btn1 = new JButton("가위");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tfMine.setText(btn1.getText());
				getResult();
			}
		});
		btn1.setBounds(21, 39, 61, 26);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("바위");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tfMine.setText(btn2.getText());
				getResult();
			}
		});
		btn2.setBounds(83, 38, 66, 29);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("보");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tfMine.setText(btn3.getText());
				getResult();
			}
		});
		btn3.setBounds(147, 39, 66, 26);
		contentPane.add(btn3);
	}
	
	public void getResult() {
		String com;
		double random = Math.random();
		if( random< 0.33) {
			com = "가위";
		}else if(random < 0.66) { 
			com = "바위";
		}else {
			com = "보";
		}
		tfCom.setText(com);
		
		String mine = tfMine.getText();
		
		String result="";
		
		if(com.equals(mine)) {
			result = "비겼습니다.";
		}else if(mine.equals("가위") && com.equals("바위")) {
			result = "졌습니다.";
		}else if(mine.equals("가위") && com.equals("보")) {
			result = "이겼습니다.";
		}else if(mine.equals("바위") && com.equals("가위")) {
			result = "이겼습니다.";
		}else if(mine.equals("바위") && com.equals("보")) {
			result = "졌습니다.";
		}else if(mine.equals("보") && com.equals("바위")) {
			result = "이겼습니다.";
		}else if(mine.equals("보") && com.equals("가위")) {
			result = "졌습니다.";
		}else {
			result = "다시입력해주세요.";
		}
		
		tfResult.setText(result);
		
		
	}

}
