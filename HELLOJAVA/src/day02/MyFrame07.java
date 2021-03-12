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

public class MyFrame07 extends JFrame {

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
					MyFrame07 frame = new MyFrame07();
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
	public MyFrame07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("내 선택");
		lblNewLabel.setBounds(21, 50, 61, 16);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("컴퓨터");
		lblNewLabel_1.setBounds(21, 105, 61, 16);
		contentPane.add(lblNewLabel_1);
		
		tfCom = new JTextField();
		tfCom.setBounds(94, 100, 130, 26);
		contentPane.add(tfCom);
		tfCom.setColumns(10);
		
		tfMine = new JTextField();
		tfMine.setBounds(94, 45, 130, 26);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		JButton btn = new JButton("결과보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String com;
				if(Math.random() < 0.5) {
					com = "홀";
				}else com = "짝";
				tfCom.setText(com);
				
				String mine = tfMine.getText();
				
				String result;
				if(com.equals(mine)) {
					result = "정답입니다.";
				}else result = "오답입니다.";
				
				tfResult.setText(result);
				
				
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
	}

}
